/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import java.util.Collection;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author agno3
 */
@Entity
@Table(name = "expert")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Expert.findAll", query = "SELECT e FROM Expert e")
    , @NamedQuery(name = "Expert.findByExpertId", query = "SELECT e FROM Expert e WHERE e.expertId = :expertId")
    , @NamedQuery(name = "Expert.findByExpertPasswd", query = "SELECT e FROM Expert e WHERE e.expertPasswd = :expertPasswd")
    , @NamedQuery(name = "Expert.findByExpertEmail", query = "SELECT e FROM Expert e WHERE e.expertEmail = :expertEmail")
    , @NamedQuery(name = "Expert.findByExpertPhone", query = "SELECT e FROM Expert e WHERE e.expertPhone = :expertPhone")
    , @NamedQuery(name = "Expert.findByExpertAvatar", query = "SELECT e FROM Expert e WHERE e.expertAvatar = :expertAvatar")
    , @NamedQuery(name = "Expert.findByExpertIdenity", query = "SELECT e FROM Expert e WHERE e.expertIdenity = :expertIdenity")
    , @NamedQuery(name = "Expert.findByExpertName", query = "SELECT e FROM Expert e WHERE e.expertName = :expertName")
    , @NamedQuery(name = "Expert.findByExpertWechat", query = "SELECT e FROM Expert e WHERE e.expertWechat = :expertWechat")
    , @NamedQuery(name = "Expert.findByExpertInfo", query = "SELECT e FROM Expert e WHERE e.expertInfo = :expertInfo")})
public class Expert implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 25)
    @Column(name = "expert_id")
    private String expertId;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 20)
    @Column(name = "expert_passwd")
    private String expertPasswd;
    @Size(max = 45)
    @Column(name = "expert_email")
    private String expertEmail;
    @Size(max = 15)
    @Column(name = "expert_phone")
    private String expertPhone;
    @Size(max = 45)
    @Column(name = "expert_avatar")
    private String expertAvatar;
    @Basic(optional = false)
    @NotNull
    @Column(name = "expert_idenity")
    private int expertIdenity;
    @Size(max = 45)
    @Column(name = "expert_name")
    private String expertName;
    @Size(max = 15)
    @Column(name = "expert_wechat")
    private String expertWechat;
    @Size(max = 256)
    @Column(name = "expert_info")
    private String expertInfo;
    @ManyToMany(mappedBy = "expertCollection")
    private Collection<Classification> classificationCollection;
    @JoinColumn(name = "mainpage_main_id", referencedColumnName = "main_id")
    @ManyToOne(optional = false)
    private Mainpage mainpageMainId;

    public Expert() {
    }

    public Expert(String expertId) {
        this.expertId = expertId;
    }

    public Expert(String expertId, String expertPasswd, int expertIdenity) {
        this.expertId = expertId;
        this.expertPasswd = expertPasswd;
        this.expertIdenity = expertIdenity;
    }

    public String getExpertId() {
        return expertId;
    }

    public void setExpertId(String expertId) {
        this.expertId = expertId;
    }

    public String getExpertPasswd() {
        return expertPasswd;
    }

    public void setExpertPasswd(String expertPasswd) {
        this.expertPasswd = expertPasswd;
    }

    public String getExpertEmail() {
        return expertEmail;
    }

    public void setExpertEmail(String expertEmail) {
        this.expertEmail = expertEmail;
    }

    public String getExpertPhone() {
        return expertPhone;
    }

    public void setExpertPhone(String expertPhone) {
        this.expertPhone = expertPhone;
    }

    public String getExpertAvatar() {
        return expertAvatar;
    }

    public void setExpertAvatar(String expertAvatar) {
        this.expertAvatar = expertAvatar;
    }

    public int getExpertIdenity() {
        return expertIdenity;
    }

    public void setExpertIdenity(int expertIdenity) {
        this.expertIdenity = expertIdenity;
    }

    public String getExpertName() {
        return expertName;
    }

    public void setExpertName(String expertName) {
        this.expertName = expertName;
    }

    public String getExpertWechat() {
        return expertWechat;
    }

    public void setExpertWechat(String expertWechat) {
        this.expertWechat = expertWechat;
    }

    public String getExpertInfo() {
        return expertInfo;
    }

    public void setExpertInfo(String expertInfo) {
        this.expertInfo = expertInfo;
    }

    @XmlTransient
    public Collection<Classification> getClassificationCollection() {
        return classificationCollection;
    }

    public void setClassificationCollection(Collection<Classification> classificationCollection) {
        this.classificationCollection = classificationCollection;
    }

    public Mainpage getMainpageMainId() {
        return mainpageMainId;
    }

    public void setMainpageMainId(Mainpage mainpageMainId) {
        this.mainpageMainId = mainpageMainId;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (expertId != null ? expertId.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Expert)) {
            return false;
        }
        Expert other = (Expert) object;
        if ((this.expertId == null && other.expertId != null) || (this.expertId != null && !this.expertId.equals(other.expertId))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.Expert[ expertId=" + expertId + " ]";
    }
    
}
