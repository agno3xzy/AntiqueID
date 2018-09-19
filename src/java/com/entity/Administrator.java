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
import javax.persistence.JoinTable;
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
@Table(name = "administrator")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Administrator.findAll", query = "SELECT a FROM Administrator a")
    , @NamedQuery(name = "Administrator.findByAdminId", query = "SELECT a FROM Administrator a WHERE a.adminId = :adminId")
    , @NamedQuery(name = "Administrator.findByAdminPasswd", query = "SELECT a FROM Administrator a WHERE a.adminPasswd = :adminPasswd")
    , @NamedQuery(name = "Administrator.findByAdminEmail", query = "SELECT a FROM Administrator a WHERE a.adminEmail = :adminEmail")
    , @NamedQuery(name = "Administrator.findByAdminIdentify", query = "SELECT a FROM Administrator a WHERE a.adminIdentify = :adminIdentify")})
public class Administrator implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 25)
    @Column(name = "admin_id")
    private String adminId;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 20)
    @Column(name = "admin_passwd")
    private String adminPasswd;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 45)
    @Column(name = "admin_email")
    private String adminEmail;
    @Basic(optional = false)
    @NotNull
    @Column(name = "admin_identify")
    private int adminIdentify;
    @JoinTable(name = "administrator_has_user", joinColumns = {
        @JoinColumn(name = "administrator_admin_id", referencedColumnName = "admin_id")}, inverseJoinColumns = {
        @JoinColumn(name = "user_user_id", referencedColumnName = "user_id")})
    @ManyToMany
    private Collection<User> userCollection;
    @JoinColumn(name = "mainpage_main_id", referencedColumnName = "main_id")
    @ManyToOne(optional = false)
    private Mainpage mainpageMainId;

    public Administrator() {
    }

    public Administrator(String adminId) {
        this.adminId = adminId;
    }

    public Administrator(String adminId, String adminPasswd, String adminEmail, int adminIdentify) {
        this.adminId = adminId;
        this.adminPasswd = adminPasswd;
        this.adminEmail = adminEmail;
        this.adminIdentify = adminIdentify;
    }

    public String getAdminId() {
        return adminId;
    }

    public void setAdminId(String adminId) {
        this.adminId = adminId;
    }

    public String getAdminPasswd() {
        return adminPasswd;
    }

    public void setAdminPasswd(String adminPasswd) {
        this.adminPasswd = adminPasswd;
    }

    public String getAdminEmail() {
        return adminEmail;
    }

    public void setAdminEmail(String adminEmail) {
        this.adminEmail = adminEmail;
    }

    public int getAdminIdentify() {
        return adminIdentify;
    }

    public void setAdminIdentify(int adminIdentify) {
        this.adminIdentify = adminIdentify;
    }

    @XmlTransient
    public Collection<User> getUserCollection() {
        return userCollection;
    }

    public void setUserCollection(Collection<User> userCollection) {
        this.userCollection = userCollection;
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
        hash += (adminId != null ? adminId.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Administrator)) {
            return false;
        }
        Administrator other = (Administrator) object;
        if ((this.adminId == null && other.adminId != null) || (this.adminId != null && !this.adminId.equals(other.adminId))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.Administrator[ adminId=" + adminId + " ]";
    }
    
}
